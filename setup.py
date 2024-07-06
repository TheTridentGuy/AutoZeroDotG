import shutil
import os
import sys


print("this script will install the autozerodotg software on your machine")
print("requirements: MacOS, sudo, Python 3.4+, watchdog (installable with this script)")
input("press enter to continue, ctrl+c to exit:")
if input("install the watchdog package y/n? ") == "y":
    print("installing watchdog...", end="")
    import pip
    pip.main(["install", "watchdog"])
    print("done")
try:
    print("making install directory...", end="")
    os.mkdir("/Library/AutoZeroDotG/")
    print("done")
    print("copying python script...", end="")
    shutil.copy("./autozerodotg.py", "/Library/AutoZeroDotG/autozerodotg.py")
    print("done")
    print("copying plist...", end="")
    shutil.copy("./com.autozero.g.plist", "/Library/LaunchDaemons/com.autozero.g.plist")
    print("done")
except PermissionError:
    print("\nplease run with sudo... exiting", file=sys.stderr)
    sys.exit(1)
print("installation complete, gcode files saved to a volume will now be automatically renamed to auto0.g")
