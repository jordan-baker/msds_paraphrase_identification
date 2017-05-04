import numpy, gzip
from cPickle import load, dump

def create():
    with gzip.open("dr-data.pickle.gz") as fin:
        D = load(fin)
        trnM, trnL = D['trnM'], D['trnL']
        tstM, tstL = D['tstM'], D['tstL']
    # Create training sample
    nRow, nDim = trnM.shape
    print('nRow, nDim = {}, {}'.format(nRow, nDim))
    trnS = numpy.zeros((nRow // 2, nDim * 2))
    for n in range(0, nRow, 2):
        if n % 1000 == 0:
            print('Process {} rows'.format(n))
        vec1, vec2 = trnM[n,:], trnM[n+1, :]
        trnS[n//2, :] = numpy.hstack((vec1+vec2, abs(vec1-vec2)))
    # Create training sample
    nRow, nDim = tstM.shape
    print('nRow, nDim = {}, {}'.format(nRow, nDim))
    tstS = numpy.zeros((nRow // 2, nDim * 2))
    for n in range(0, nRow, 2):
        if n % 1000 == 0:
            print('Process {} rows'.format(n))
        vec1, vec2 = tstM[n,:], tstM[n+1, :]
        tstS[n//2, :] = numpy.hstack((vec1+vec2, abs(vec1-vec2)))
    # Save data
    D = {'trnM':trnS, 'trnL':trnL,
         'tstM':tstS, 'tstL':tstL}
    with gzip.open("clf-data.pickle.gz", "w") as fout:
        dump(D, fout)
    print('Done')


if __name__ == '__main__':
    create()