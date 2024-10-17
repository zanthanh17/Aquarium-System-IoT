import lib.umail as umail

sender_email='thanhpm175@gmail.com'
sender_name='PBL3'
sender_app_password='onkt buld ggrx juph'
recipient_email='vanthanh1752k3@gmail.com'
#Hàm gửi email
def send_email(sender_email, sender_name, sender_app_password, recipient_email, email_subject, email_message):
    try:
        smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True)  # Gmail's SSL port
        smtp.login(sender_email, sender_app_password)
        smtp.to(recipient_email)
        smtp.write("From:" + sender_name + "<" + sender_email + ">\n")
        smtp.write("Subject:" + email_subject + "\n")
        smtp.write(email_message)
        smtp.send()
        smtp.quit()
        
    except Exception as e:
        print(f'Failed to send email: {e}')
        
def warning(temp,NTU,pH):
    if temp > 31:
        email_subject = 'Thông báo chất lượng nước'
        email_message = 'Nhiệt độ nước của bạn hiện tại là ' + str(temp) + '°C'" \n"
        
        send_email(sender_email, sender_name, sender_app_password, recipient_email,email_subject,email_message)
        print('Đã gửi email cảnh báo pH bất thường') 
        
    if pH > 8 or pH < 6:
        email_subject = 'Thông báo chất lượng nước'
        email_message = 'Độ pH nước của bạn hiện tại là ' + str(pH) +  "\n"
        
        send_email(sender_email, sender_name, sender_app_password, recipient_email,email_subject,email_message)
        print('Đã gửi email cảnh báo pH bất thường')
    
    if NTU > 500:
        email_subject = 'Thông báo chất lượng nước'
        email_message = 'Độ đục nước của bạn hiện tại là ' + str(NTU) + ' NTU'" \n"
        
        send_email(sender_email, sender_name, sender_app_password, recipient_email,email_subject,email_message)
        print('Đã gửi email cảnh báo NTU bất thường')