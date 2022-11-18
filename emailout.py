import win32com.client

outlook = win32com.client.Dispatch('outlook.application')

def emailout(emailids):
    for i,emailid in enumerate(emailids):
        mail = outlook.CreateItem(0)
        mail.To = emailid
        mail.Subject = 'The most awaited hackathon is here! TCS HackQuest!'
        mail.HTMLBody = '<h2>Dear user, please find the attached price comparison sheet as requested.</h2>' #this field is optional

        # To attach a file to the email (optional):
        attachment  = "C:/Users/kvyk/Downloads/" + emailid + f"{i}.xlsx"
        mail.Attachments.Add(attachment)

        mail.Send()