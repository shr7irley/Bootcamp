import subprocess
# operación a realizar
ioR = input("Enter operation (install/remove): ").lower()
# paquetes por defecto
defaultPackages = "vim curl wget"
print("Enter a list of packages to install")
print("The list should be separated by spaces, for example:")
print(" package1 package2 package3")
print("Otherwise, input 'default' to " + ioR + " the default packages listed in this program")
packages = input().lower()
if packages == "default":
    packages = defaultPackages
# convertir paquetes a lista
package_list = packages.split()
if ioR == "install":
    subprocess.run(["sudo", "apt-get", "install"] + package_list)
elif ioR == "remove":
    while True:
        print("Purge files after removing? (Y/N)")
        choice = input().upper()
        if choice == "Y":
            subprocess.run(["sudo", "apt-get", "--purge"] + package_list)
            break
        elif choice == "N":
            subprocess.run(["sudo", "apt-get", "remove"] + package_list)
            break
    subprocess.run(["sudo", "apt", "autoremove"])
else:
    print("Invalid option")
