import mypackage
import mypackage.mylib
import mypackage.sub.sublib as sl

ret1 = mypackage.mylib.add_txt('대한민국','1등')
ret2 = mypackage.mylib.reverse('r','e','v','e','r','s')

ret3 = sl.add_num(10,12)

print("""ret1 = %s
ret2 = %s
ret3 = %d"""
%(ret1,ret2,ret3))
