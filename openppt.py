

def openppt():
    import platform
    import subprocess

    filename = "shapes-test.pptx"

    if platform.system() == 'Windows':
        subprocess.call(('cmd', '/C', filename))
    elif platform.system() == 'Linux':
        subprocess.call(('xdg-open', filename))
    elif platform.system() == 'Darwin':
        subprocess.call(('open', filename))