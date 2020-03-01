import cv2
import numpy

def generate(end):
    seq = [0]
    for n in range(1, end):
        an = seq[-1] - n
        an = an if (an not in seq) and (an > 0) else seq[-1] + n 
        seq.append(an)
    return seq

if __name__ == '__main__':

    width, hgt = (1500, 800)
    img = numpy.ones((hgt, width, 3)) * 255

    seq = generate(hgt//8)
    offset_x = 70
    color = [255, 0, 255]
    for i in range(len(seq) - 1):
        # color = numpy.uint8(numpy.random.random(3) * 255)
        df = (seq[i] - seq[i + 1])
        radius = abs(df) * 3
        axes = (radius, radius) 

        if df > 0:
            angle = 0
        else:
            angle = 180

        startAngle = 0
        endAngle   = 180
        center     = (offset_x + (seq[i] + seq[i+1]) * 3, hgt//2)
        
        cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color)
        cv2.imshow("Recaman's sequence", img)
        k = cv2.waitKey(10)
        if k == 27:
            break
        elif k == ord(' '):
            cv2.waitKey(0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

