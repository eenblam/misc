mkdir ~/local
cd ~/Downloads

wget https://gmplib.org/download/gmp/gmp-6.1.0.tar.xz
tar --xz -xvf gmp-6.1.0.tar.xz
cd gmp-6.1.0/
.configure --prefix=/home/ben/local
# -j4 for 4 processors; adapt as needed.
make -j4
make install
cd ..

wget http://www.mpfr.org/mpfr-current/mpfr-3.1.3.tar.xz
tar --xz -xvf mpfr-2.3.0.tar.xz
cd mpfr-2.3.0
./configure --prefix=/home/ben/local --with-gmp=/home/ben/local
make -j4
make install
cd ..

wget ftp://ftp.gnu.org/gnu/mpc/mpc-1.0.3.tar.gz
tar -xzvf mpc-1.0.3.tar.gz
cd mpc-1.0.3
./configure --prefix=/home/ben/local --with-gmp=/home/ben/local --with-mpfr=/home/ben/local
make -j4
make install
cd ..

# Finally, get gcc and then untar, configure and build it as follows:
#TODO Why did I go for a newer gcc / ignore apt?
wget ftp://ftp.gnu.org/gnu/gcc/gcc-5.3.0/gcc-5.3.0.tar.bz2
tar -xjf gcc-4.2.2.tar.bz2 #TODO Why do versions not match? What was I doing?
mkdir build
cd build
../gcc-4.2.2/configure --prefix=/home/ben/local \
--with-gmp=/home/ben/local \
--with-mpfr==/home/ben/local \
--with-mpc==/home/ben/local \
--enable-languages=c,c++,fortran \
--disable-multilib

time make -j8 bootstrap
make install

export LD_LIBRARY_PATH=/home/ben/local/lib64

ln -s /home/ben/local/lib64/libgomp.spec /home/ben/local/lib/libgomp.spec

echo "if [ -d "$HOME/local/lib64" ] ; then export LD_LIBRARY_PATH="$HOME/local/lib64" ; fi" >> ~/.profile
