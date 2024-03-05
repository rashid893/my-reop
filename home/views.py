from django.shortcuts import render
from .models import CompanyBooking,Deal,Module3
from django.contrib import messages
from datetime import datetime


# Create your views here.
def home(request):
    return render(request,'home.html')



def module1(request):
    if request.method == 'POST':
        # Retrieve data from the form
        company_bookings = request.POST.get('client')
      
        manual_bilty = request.POST.get('manual_bilty')
        customer_order_number = request.POST.get('customer_order_number')
        booking_price = request.POST.get('booking_price')
        vehicle_number = request.POST.get('vehicle_number')
        drivers_name = request.POST.get('drivers_name')
        drivers_id = request.POST.get('drivers_id')
        drivers_mobile = request.POST.get('drivers_mobile')
        pending_at_company = request.POST.get('pending_at_company')
        product = request.POST.get('product')
        products_bank_payment_slip_number = request.POST.get('products_bank_payment_slip_number')
        payment_amount = request.POST.get('payment_amount')
        order_amount = request.POST.get('order_amount')
        name_of_the_bank = request.POST.get('name_of_the_bank')
        zafar_and_brothers_bank_account_number = request.POST.get('zafar_and_brothers_bank_account_number')
        target_bank_account = request.POST.get('target_bank_account')
        warehouse_booking = request.POST.get('warehouse_booking')
        invoice_picture = request.FILES.get('invoice_picture')
        status = request.POST.get('reach_return')
        tons = request.POST.get('tons')
        ordered_total_bags = request.POST.get('ordered_total_bags')
        print("heeeereeeeeee is data",company_bookings,booking_price,drivers_name,invoice_picture)

        # Create a CompanyBooking object and save it to the database
        company_booking =CompanyBooking(
            Company_Bookings=company_bookings,
            
            builty_number =manual_bilty,
            customer_order_number=customer_order_number,
            booking_price=booking_price,
            vehicle_number=vehicle_number,
            drivers_name=drivers_name,
            drivers_id=drivers_id,
            drivers_mobile=drivers_mobile,
            pending_at_company=pending_at_company,
            product=product,
            bank_payment_slip_number=products_bank_payment_slip_number,
            payment_amount=payment_amount,
            order_amount=order_amount,
            name_of_the_bank=name_of_the_bank,
            zafar_and_brothers_bank_account_number=zafar_and_brothers_bank_account_number,
            target_bank_account=target_bank_account,
            warehouse_booking=warehouse_booking,
            invoice_picture=invoice_picture,
            status=status,
            tons=tons,
            ordered_total_bags=ordered_total_bags
        )
        company_booking.save()
        messages.success(request, 'Data added successfully')
        return render(request,'module1.html')

        # Redirect to a success page or return a success message
    return render(request,'module1.html')
from datetime import datetime
from .models import Deal  # Replace 'Deal' with your actual model





def module2(request):
    if request.method == 'POST':
        trader_name = request.POST.get('client')
       
        deal_price = request.POST.get('deal_price')
        vehicle_number = request.POST.get('vehicle_number')
        drivers_name = request.POST.get('drivers_name')
        drivers_id = request.POST.get('drivers_id')
        stock_location = request.POST.get('stock_location')
        delivered_status = request.POST.get('delevery')
        drivers_mobile = request.POST.get('drivers_mobile')
        tons = request.POST.get('tons')
        ordered_bags = request.POST.get('ordered_total_bags')
        pending_ordered_bags = request.POST.get('pending_at_company')
        delivered_bags = request.POST.get('deliveredbags')
        dispatched = request.POST.get('dispatchedStatus')
        product = request.POST.get('product')
        bank_payment_slip_number = request.FILES.get('products_bank_payment_slip_number')
        payment_type = request.POST.get('paymentType')
        payment_amount = request.POST.get('payment_amount')
        order_total_amount = request.POST.get('order_amount')
        payment_expected_date = request.POST.get('expec_date')
        bank_name = request.POST.get('name_of_the_bank')
        zafar_and_brothers_account_number = request.POST.get('zafar_and_brothers_bank_account_number')
        target_trader_account = request.POST.get('target_bank_account')
        warehouse_booking = request.POST.get('warehouse_booking')
        fare_paid_by = request.POST.get('fareedby')
        invoice_picture = request.FILES.get('invoice_picture')
        freight_paid = request.POST.get('freight-paid')
        status = request.POST.get('reach_return')
        print("xxxxxxxxxxxxxxxxxxxxx",trader_name,freight_paid)
           # Check if the payment type is "Hawala" and get the payment details
        if payment_type == 'Hawala':
            payment_type  = request.POST.get('paymentDetails')
            print("hereeeeeeeeeeeeee is hawala ",payment_type )
        else:
            payment_type =payment_type 

        
        
       
        deal = Deal(
            trader_name=trader_name,
          
            deal_price=deal_price,
            vehicle_number=vehicle_number,
            drivers_name=drivers_name,
            drivers_id=drivers_id,
            stock_location=stock_location,
            delivered_status=delivered_status,
            drivers_mobile=drivers_mobile,
            tons=tons,
            ordered_bags=ordered_bags,
            pending_ordered_bags=pending_ordered_bags,
            delivered_bags=delivered_bags,
            dispatched=dispatched,
            product=product,
            bank_payment_slip_number=bank_payment_slip_number,
            payment_type=payment_type,
            payment_amount=payment_amount,
            order_total_amount=order_total_amount,
            payment_expected_date=payment_expected_date,
            bank_name=bank_name,
            zafar_and_brothers_account_number=zafar_and_brothers_account_number,
            target_trader_account=target_trader_account,
            warehouse_booking=warehouse_booking,
            fare_paid_by=fare_paid_by,
            invoice_picture=invoice_picture,
            freight_paid=freight_paid,
            status=status
        )

        deal.save()

        messages.success(request, 'Data added successfully.')
        return render(request, 'module2.html') # Redirect to the same page or another page
    else:
        return render(request, 'module2.html')
 
 ################ MODULE 3 #############################################33



def module3(request):

    if request.method == 'POST':
        trader_name = request.POST.get('client')
       
        deal_price = request.POST.get('deal_price')
        deal_freight = request.POST.get('deal-freight')
        third_party_name = request.POST.get('third_party_name')
        third_party_paid_fare = request.POST.get('third_party_paid_fare')
        paid_by_self = request.POST.get('paid_by-self')
        owner_transport_fare = request.POST.get('owner_transport_fare')

        
        vehicle_number = request.POST.get('vehicle_number')
        drivers_name = request.POST.get('drivers_name')
        drivers_id = request.POST.get('drivers_id')
        stock_location = request.POST.get('stock_location')
        delivered_status = request.POST.get('delevery')
        drivers_mobile = request.POST.get('drivers_mobile')
        tons = request.POST.get('tons')
        ordered_bags = request.POST.get('ordered_total_bags')
        pending_ordered_bags = request.POST.get('pending_at_company')
        delivered_bags = request.POST.get('deliveredbags')
        dispatched = request.POST.get('dispatchedStatus')
        product = request.POST.get('product')
        bank_payment_slip_number = request.FILES.get('products_bank_payment_slip_number')
        payment_type = request.POST.get('paymentType')
        payment_amount = request.POST.get('payment_amount')
        order_total_amount = request.POST.get('order_amount')
        payment_expected_date = request.POST.get('expec_date')
        bank_name = request.POST.get('name_of_the_bank')
        zafar_and_brothers_account_number = request.POST.get('zafar_and_brothers_bank_account_number')
        target_trader_account = request.POST.get('target_bank_account')
        warehouse_booking = request.POST.get('warehouse_booking')
        fare_paid_by = request.POST.get('fareedby')
        invoice_picture = request.FILES.get('invoice_picture')
        freight_paid = request.POST.get('freight-paid')
        status = request.POST.get('reach_return')
        print("xxxxxxxxxxxxxxxxxxxxx",trader_name,freight_paid)
           # Check if the payment type is "Hawala" and get the payment details
        if payment_type == 'Hawala':
            payment_type  = request.POST.get('paymentDetails')
            print("hereeeeeeeeeeeeee is hawala ",payment_type )
        else:
            payment_type =payment_type 

        
        
       
        deal = Module3(
            trader_name=trader_name,
          
            deal_price=deal_price,
            deal_freight=deal_freight,
            third_party_name=third_party_name,
            thrid_party_paid_fare=third_party_paid_fare,
            paid_by_self=paid_by_self,
            owner_transport_fare=owner_transport_fare,
            vehicle_number=vehicle_number,
            drivers_name=drivers_name,
            drivers_id=drivers_id,
            stock_location=stock_location,
            delivered_status=delivered_status,
            drivers_mobile=drivers_mobile,
            tons=tons,
            ordered_total_bags=ordered_bags,
            pending_ordered_bags_at_traders_area =pending_ordered_bags,
            delivered_bags=delivered_bags,
            dispatched=dispatched,
            product=product,
            bank_payment_slip_number=bank_payment_slip_number,
            payment_type=payment_type,
            payment_amount=payment_amount,
            order_total_amount=order_total_amount,
            payment_expected_date=payment_expected_date,
            bank_name=bank_name,
            zafar_and_brothers_account_number=zafar_and_brothers_account_number,
            target_trader_account=target_trader_account,
            warehouse_booking=warehouse_booking,
            fare_paid_by=fare_paid_by,
            invoice_picture=invoice_picture,
            freight_paid=freight_paid,
            status=status
        )

        deal.save()

        messages.success(request, 'Data added successfully.')
        return render(request, 'module3.html') # Redirect to the same page or another page
    else:
        return render(request, 'module3.html')

    

