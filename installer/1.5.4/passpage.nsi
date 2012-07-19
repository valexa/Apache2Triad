[Settings]
NumFields=9

[Field 1]
Type=Icon
Left=0
Right=20
Top=0
Bottom=20

[Field 2]
Type=Label
Left=25
Right=-3
Top=0
Bottom=30
Text="On this page you can setup the global password that will be used mostly in corelattion with the 'root' username in many of the Apache2Triad components ."

[Field 3]
Type=Groupbox
Left=2
Right=-2
Top=40
Bottom=95
Text= Set Password

[Field 4]
Type=Label
Left=20
Right=100
Top=56
Bottom=66
Text=Enter new Password :

[Field 5]
Type=Label
Left=20
Right=100
Top=76
Bottom=86
Text=Re-enter Password :

[Field 6]
Type=Password
Left=100
Right=-20
Top=56
Bottom=66
MinLen=8
MaxLen=32
ValidateText=Bad password lenght !

[Field 7]
Type=Password
Left=100
Right=-20
Top=76
Bottom=86
MinLen=8
MaxLen=32
ValidateText=Bad password lenght !

[Field 8]
Type=Label
Left=2
Right=110
Top=110
Bottom=120
Text=Minimum password lenght: 8

[Field 9]
Type=Label
Left=2
Right=110
Top=121
Bottom=132
Text=Maximum password lenght: 32
