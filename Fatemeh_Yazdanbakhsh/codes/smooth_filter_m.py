import itk

def smooth_2d(image_input,sigma):
    PixelType = itk.ctype('signed short')
    Dimension = 2

    ImageType = itk.Image[PixelType, Dimension]
    smoothFilter = itk.SmoothingRecursiveGaussianImageFilter[
        ImageType,
        ImageType].New()
    smoothFilter.SetInput(image_input)
    smoothFilter.SetSigma(sigma)
    smoothFilter.Update()
    w = image_input.GetLargestPossibleRegion().GetSize()[0]
    h = image_input.GetLargestPossibleRegion().GetSize()[1]
    smoothed_image=smoothFilter.GetOutput()
    return smoothed_image


def smooth_3d(image_input,sigma):
    PixelType =  itk.ctype('signed short')
    Dimension = 3

    ImageType = itk.Image[PixelType, Dimension]
    smoothFilter = itk.SmoothingRecursiveGaussianImageFilter[
        ImageType,
        ImageType].New()
    smoothFilter.SetInput(image_input)
    smoothFilter.SetSigma(sigma)
    smoothFilter.Update()
    w = image_input.GetLargestPossibleRegion().GetSize()[0]
    h = image_input.GetLargestPossibleRegion().GetSize()[1]
    d = image_input.GetLargestPossibleRegion().GetSize()[2]
    smoothed_volume=smoothFilter.GetOutput()
    return smoothed_volume
