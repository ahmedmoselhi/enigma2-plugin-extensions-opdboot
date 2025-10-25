from distutils.core import setup
import setup_translate


setup(name='enigma2-plugin-extensions-opdboot',
		version='3.1',
		author='formiano/ahmedmoselhi',
		author_email='ahmedmoselhi55@gmail.com',
		package_dir={'Extensions.OPDBoot': 'src'},
		packages=['Extensions.OPDBoot'],
		package_data={'Extensions.OPDBoot': ['*.mvi', '*.png', 'images/*.png', 'ubi_reader/*', 'ubi_reader/ubi/*', 'ubi_reader/ubi/volume/*', 'ubi_reader/ubi/headers/*', 'ubi_reader/ubi/block/*', 'ubi_reader/ubifs/*', 'ubi_reader/ubifs/nodes/*', 'ubi_reader/ubi_io/*', 'ubi_reader/ui/*', 'bin/*', 'OPDBoot_client/*', 'OPDBoot_client/images/*.png']},
		description='OPD MultiBoot',
		cmdclass=setup_translate.cmdclass)
