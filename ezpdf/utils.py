import os


def import_bocr(v):
    try:
        import bocr
        v['bocr'] = vars()['bocr']
        return bocr

    except:
        if not os.path.exists('../bocr'):
            raise FileExistsError('The package bocr is not found!')
        import sys
        sys.path.append('../bocr')
        import bocr
        v['bocr'] = vars()['bocr']
        return bocr

