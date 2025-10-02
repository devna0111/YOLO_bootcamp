# conda activate cv

def fastcorner() :
    import cv2
    src = cv2.imread('img/building.jpg', cv2.IMREAD_GRAYSCALE)

    fast = cv2.FastFeatureDetector_create(60)
    keypoints = fast.detect(src)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    for kp in keypoints:
        pt = (int(kp.pt[0]), int(kp.pt[1]))
        cv2.circle(dst, pt, 5, (0, 0, 255), 2)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    fastcorner()