def draw_test() :
    import numpy as np
    import cv2

    data = np.full((120,120,3),(0,0,0),dtype=np.uint8) # unsigned interger8
    # data = np.zeros_like((120,120,3),dtype=np.uint8)
    print(data)
    data[60:,:] = 255
    cv2.rectangle(data,(0,40),(120,60),(255,100,100),-1)
    cv2.rectangle(data,(0,80),(120,100),(100,100,255),-1)
    cv2.rectangle(data,(30,0),(50,120),(255,255,255),-1)
    cv2.rectangle(data,(70,0),(90,120),(255,255,255),-1)
    cv2.line(data,(40,0),(40,120),(150,150,150),10)
    cv2.line(data,(80,0),(80,120),(50,150,50),10)
    cv2.line(data,(0,40),(120,40),(50,50,150),10)
    cv2.line(data,(0,80),(120,80),(150,50,50),10)

    cv2.imshow('data',data)

    cv2.waitKey()
    cv2.destroyAllWindows()

def draw_test2() :
    import numpy as np
    import cv2 
    data = np.array(np.arange(1,10)).reshape(3,-1)
    data = np.vstack((data,data))
    print(data)

def draw_test3() :
    import numpy as np
    import cv2 
    data = np.array([[1,2,3]]*3 + [[4,5,6]]*3)
    print(data)

def draw_test4() :
    import numpy as np
    data = np.arange(10,20)
    # print(data[data >=15])
    print(np.where(data > 15, 99,data))
    print(data[data>15])
    print(data)

def draw_test5() :
    import cv2
    import matplotlib.pyplot as plt
    img = cv2.imread('./img/girl.jpg')
    plt.imshow(img)
    plt.show()
    
# if __name__ == "__main__" :
    # draw_test()
    # import numpy as np
    # print(np.zeros_like((120,120,3)))
    # draw_test3()
    # draw_test4()
    # draw_test5()

import numpy as np
import cv2
from PIL import Image

# _, dst = cv2.threshold()
# dst_adap = cv2.adaptiveThreshold()

print(cv2.getStructuringElement(3,1,(-1,-1)))

