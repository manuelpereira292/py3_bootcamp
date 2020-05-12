import sys

print('Distance to convert:')
distance =  sys.stdin.readline().rstrip()

print('Input measurement standard (in, ft, mi):')
mes_in =  sys.stdin.readline().rstrip()

print('Output measurement standard (mm, m, km):')
mes_out =  sys.stdin.readline().rstrip()

in_value = float(distance)

if mes_in == 'in':
    pass

elif mes_in == 'ft':
    in_value = 12 * in_value

elif mes_in == 'mi':
    in_value = 12 * 63360


if mes_out == 'mm':
    out_value= in_value * 25.4

elif mes_out == 'm':
    #out_value= in_value * 25.4 * 0.001
    out_value= in_value * 0.0254

elif mes_out == 'km':
    #out_value= in_value * 25.4 * 0.001* 0.001
    out_value= in_value * 0.0000254

print(distance + mes_in + ' ---> ' + str(out_value) + mes_out )
