cd $DAFOAM_ROOT_PATH/packages && \
wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh && \
chmod 755 Miniconda3-py38_4.10.3-Linux-x86_64.sh && \
./Miniconda3-py38_4.10.3-Linux-x86_64.sh -b -p $DAFOAM_ROOT_PATH/packages/miniconda3 && \
echo '# Miniconda3' >> $DAFOAM_ROOT_PATH/loadDAFoam.sh && \
echo 'export PATH=$DAFOAM_ROOT_PATH/packages/miniconda3/bin:$PATH' >> $DAFOAM_ROOT_PATH/loadDAFoam.sh && \
echo 'export LD_LIBRARY_PATH=$DAFOAM_ROOT_PATH/packages/miniconda3/lib' >> $DAFOAM_ROOT_PATH/loadDAFoam.sh && \
echo 'export PYTHONUSERBASE=no-local-libs' >> $DAFOAM_ROOT_PATH/loadDAFoam.sh && \
. $DAFOAM_ROOT_PATH/loadDAFoam.sh