from matplotlib import font_manager
for f in font_manager.findSystemFonts(fontpaths=None, fontext='ttf'):
    if "msyh" in f.lower() or "simhei" in f.lower():
        print(f)
