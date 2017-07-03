import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

publishKey = settings.STRIPE_PUBLISHABLE_KEY
stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.

@login_required
def checkout(request):
    if request.method == "POST":
        print("**************: ",request.POST)
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
