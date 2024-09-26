import blynklib_mp

BLYNK_TEMPLATE_ID = "TMPL6Z78zEeyN"
BLYNK_TEMPLATE_NAME = "PBL3"
BLYNK_AUTH_TOKEN = "ntlI3mfVTq7OGbENwVtmV6VG89xuipbK"

def connect_blynk(blynk):
    if blynk is None:
        print('Failed to initialize Blynk')
    else:
        print('Blynk initialized successfully')

def display_blynk(blynk,NTU,phValue):
    if blynk is not None:
        blynk.virtual_write(1,NTU)
        blynk.virtual_write(2,phValue)
        # blynk.virtual_write(0,temp)
        blynk.run()