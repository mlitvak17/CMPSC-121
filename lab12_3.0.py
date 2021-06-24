#LAB 12 CMPSC 121 SPRING 2017
#Name: Mauricio Litvak

def house_flip(pp, ecor, etr, erp, cair, cr, fcoc):
    print('-------------------------------------')
    ccop = fcoc + (.01*pp)
    print('Closing costs on purchase: $%.2f' % ccop)
    dp = .2 * pp
    print('Down Payment: $%.2f' % dp)
    ioma = pp - dp + ccop
    print('Interest only mortgage amount: $%.2f' % ioma)
    tcomi = (dp * cair) / (12 / etr)
    print('Total cost of money invested: $%.2f' % tcomi)
    iol = (ioma * cair * etr) / 12
    print('Interest on loan: $%.2f' % iol)
    sc = cr * erp
    print('Sales commission: $%.2f' % sc)
    ccos = erp * .01
    print('Closing costs on sale: $%.2f' % ccos)
    tpod = erp - (pp + ecor + iol + sc + ccos + tcomi + ccop)
    if tpod < 0:
        tpod = tpod * -1
        print('You did not make money, you are in the RED.')
        print('CONGRATULATIONS! You lost $%.2f' % tpod)
    else:
        print('Total profit on deal: $%.2f' % tpod)
    
purchase_price = float(input('Purchase Price: $'))
estimated_cost_of_repairs = float(input('Estimated Cost of Repairs: $'))
estimated_time_repair = int(input('Estimated Time to Complete Repairs (in months): '))
estimated_resale_price = float(input('Estimated Resale Price: $'))
current_ann_int_rate = float(input('Current Annual Interest Rate: ')) / 100
comm_rate = float(input('Commission Rate on Sale of House: ')) / 100
fixed_cost_of_close = float(input('Fixed Cost of Closing: $'))

house_flip(purchase_price, estimated_cost_of_repairs, estimated_time_repair, estimated_resale_price, current_ann_int_rate, comm_rate, fixed_cost_of_close)
