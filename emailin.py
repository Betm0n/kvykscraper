import os
import win32com.client

path = os.path.expanduser("C:/Users/kvyk/Downloads/")  

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")  #opens outlook
inbox = outlook.GetDefaultFolder(6) 
messages = inbox.Items


def emailin():
    try:
        filename = []
        if(True):
            for message in messages:
                if message.Unread:
                    attachments = message.Attachments
                    attachment = attachments.Item(1)
                    for attachment in message.Attachments:
                        filename.append(message.SenderEmailAddress)
                        attachment.SaveAsFile(os.path.join(path, str(filename[-1] + f'{len(filename)-1}.xlsx')))
                    message.Unread = False #marking the email as read after downloading the attachment
        return filename
    except:
        print('There is no new email')
        print('Exiting')
        exit()