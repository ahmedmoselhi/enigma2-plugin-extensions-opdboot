from distutils.core import setup
import setup_translate


setup(name='enigma2-plugin-extensions-opdboot',
		version='3.1',
		author='formiano/ahmedmoselhi',
		author_email='ahmedmoselhi55@gmail.com',
		package_dir={'Extensions.OPDBoot': 'src'},
		packages=['Extensions.OPDBoot'],
		package_data={'Extensions.OPDBoot': ['*.mvi', '*.png', 'images/*.png', 'ubi_reader/*', 'OPDBoot_client/*', 'bin/*']},
		description='OPD MultiBoot',
		cmdclass=setup_translate.cmdclass)
