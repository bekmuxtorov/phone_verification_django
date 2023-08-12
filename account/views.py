from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
# from .sent_sms import sent_sms_to_phone_number
from .sent_sms_infobip import sent_sms_to_phone_number


@api_view(['POST'])
def sent_verification_code(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response(
            {
                'status': 400,
                'message': 'Phone number is required'
            }
        )

    if data.get('password') is None:
        return Response(
            {
                'status': 400,
                'message': 'Password is required'
            }
        )

    phone_number = data.get('phone_number')
    if len(phone_number) != 9:
        return Response(
            {
                'status': 400,
                'message': "The phone number must be entered as follows: 901234567"
            }
        )
    phone_number = ''.join(['998', phone_number])

    try:
        user = User.objects.create(
            phone_number=phone_number,
            verification_code=sent_sms_to_phone_number(
                phone_number=phone_number
            )
        )
        user.set_password = data.get('set_password')
        user.save()

    except Exception:
        user = User.objects.get(phone_number=phone_number)
        user.verification_code = sent_sms_to_phone_number(
            phone_number=phone_number
        )
        user.save()

    return Response(
        {
            'status': 200,
            'message': 'Code sent'
        }
    )


@api_view(['POST'])
def verify_code(request):
    data = request.data
    if data.get('phone_number') is None:
        return Response(
            {
                'status': 400,
                'message': 'Phone number is required'
            }
        )

    if data.get('code') is None:
        return Response(
            {
                'status': 400,
                'message': 'code is required'
            }
        )
    phone_number = data.get('phone_number')
    if len(phone_number) != 9:
        return Response(
            {
                'status': 400,
                'message': "The phone number must be entered as follows: 901234567"
            }
        )
    phone_number = ''.join(['998', phone_number])

    if not User.objects.filter(phone_number=phone_number).exists():
        return Response(
            {
                'status': 400,
                'message': 'Invalid phone number'
            }
        )
    user = User.objects.filter(phone_number=phone_number).first()

    if user.verification_code == int(data.get('code')):
        user.is_phone_verified = True
        user.save()
        return Response({
            'status': 200,
            'message': 'Verify code'
        })

    return Response({
        'status': 400,
        'message': 'Invalid code'
    })
