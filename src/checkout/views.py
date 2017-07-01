import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY
# stripe.api_key = "sk_test_whc6atzMhM3uV499rqg2Q6G7"


# Create your views here.

@login_required
def checkout(request):
    template = 'checkout.html'
    context = {'context':stripe.api_key}
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
