#%%
import smtplib
def send_mail(len):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("nukahn@gmail.com", "rwhctklgntjgjrqe")
    # message to be sent
    if(len == 0):
        message = ("검색이 시작되었습니다.").encode('utf-8')
    else:
        message = ("새로운 상품이 "+ str(len) + " 개 등록 되었습니다.").encode('utf-8')
    # sending the mail
    s.sendmail("nukahn@gmail.com", "nukahn@infinistar.co.kr", message)
    # terminating the session
    s.quit()

