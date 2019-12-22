from django.shortcuts import render


# define get_offer function, to get 'offer' and 'price' field from a model \
# and calcuate final price
def get_offer(obj):
    if obj.offer:
        if obj.offer.type == 'percent':
            try:
                offer_price = int(int(obj.price) - (int(obj.price) * (int(obj.offer.amount) / 100)))
            except:
                pass
            else:
                return offer_price

        elif obj.offer.type == 'absolute':
            try:
                offer_price = int(obj.price) - int(obj.offer.amount)
            except:
                pass
            else:
                return offer_price
    else:
        offer_price = False
