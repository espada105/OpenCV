using System;
using OpenCvSharp;

class Program
{
    static void Main(string[] args)
    {
        Mat img = Cv2.ImRead("../.data/apple.webp");
        
        Mat gray = new Mat();
        Cv2.CvtColor(img, gray, ColorConversionCodes.BGR2GRAY);
        
        CircleSegment[] circles = Cv2.HoughCircles(
            gray,
            HoughModes.Gradient,
            1,
            200,
            param1: 150,
            param2: 20,
            minRadius: 50,
            maxRadius: 120
        );
        
        if (circles != null)
        {
            foreach (CircleSegment circle in circles)
            {
                Point center = new Point(circle.Center.X, circle.Center.Y);
                
                Cv2.Circle(
                    img,
                    center,
                    (int)circle.Radius,
                    new Scalar(255, 0, 0),
                    2,
                    LineTypes.AntiAlias
                );
            }
        }
        
        using (new Window("Circle Detection", img))
        {
            Cv2.WaitKey();
        }
    }
}