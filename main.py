from hashing import get_pbo_hashes, get_longhash, get_shorthash

MOD_PATH = r'D:\Steam\steamapps\common\Arma 3\GM'


def main():
    hashes = get_pbo_hashes(MOD_PATH)
    longhash = get_longhash(hashes)
    shorthash = get_shorthash(longhash)

    print(longhash)
    print(shorthash)


if __name__ == '__main__':
    main()
