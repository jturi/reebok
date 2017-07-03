from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.

@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == "POST":
        print("**************: ",request.POST)
        token = request.POST['stripeToken']
        print("**************Token: ", token)
        try:
            charge = stripe.Charge.create(
                amount=2000,
                currency="usd",
                source=token, # obtained with Stripe.js
                metadata={'order_id': '7777'}
            )
        except stripe.error.CardError as e:
            # The card has been declined
            pass
    template = 'checkout.html'
    context = {'publishKey':publishKey}
    return render(request, template, context)



    # publishKey = settings.STRIPE_PUBLISHABLE_KEY
    # if request.method == 'POST':
    #     token = request.POST['stripeToken']
    #     print("stripeToken:", token)
    # context = {'publishKey': publishKey}
    # template = 'checkout.html'
    # return render(request, template, context)


# stripe.Charge.create(
#     amount=2000,
#     currency="usd",
#     source="tok_1AamWVKnLOwnICsycF2qjImc",  # obtained with Stripe.js
#     metadata={'order_id': '6735'}
# )
