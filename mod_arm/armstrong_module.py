import arm_mod

arm_mod.step()
low = int(input("\n\n\tEnter lower limit: "))
up = int(input("\tEnter upper limit: "))
print("\tArmstrong numbers are: ")
arm_mod.arm(low, up)
