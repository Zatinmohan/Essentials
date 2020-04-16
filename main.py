import os

if __name__ == '__main__':
    folders = os.listdir("E:\images")
    dir = 'E:\images\\'
    for content in folders:
        x = os.listdir(dir + content)

        l = 1;
        for filename in os.listdir(dir+content):
            os.rename(dir+content+'\\'+filename,dir+content+'\\'+l.__str__()+".png")
            l+=1
