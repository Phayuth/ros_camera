from pypylon import pylon

tl_factory = pylon.TlFactory.GetInstance()

cam = None
for dev_info in tl_factory.EnumerateDevices():
    if dev_info.GetDeviceClass() == 'BaslerGigE':
        print("using %s @ %s" % (dev_info.GetModelName(), dev_info.GetIpAddress()))
        cam = pylon.InstantCamera(tl_factory.CreateDevice(dev_info))
        
else:
    raise EnvironmentError("no GigE device found")