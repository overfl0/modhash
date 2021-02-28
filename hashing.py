import binascii
import hashlib
import os


def BIHash_bytes(key):
    """RSHash, but not really :P"""
    b = 63689
    a = 378551
    hash = 0
    for c in key:
        hash = (hash * a + c) & 0xffffffff
        a = (a * b) & 0xffffffff
    return hash


def BIHash(key):
    """RSHash, but not really :P"""
    b = 63689
    a = 378551
    hash = 0
    for i in range(len(key)):
        hash = (hash * a + ord(key[i])) & 0xffffffff
        a = (a * b) & 0xffffffff
    return hash


def get_pbo_sha1_hash(path):
    with open(path, 'rb') as f:
        f.seek(-20, 2)
        hash = f.read()
        hash = binascii.hexlify(hash)

    return hash


def get_pbo_hashes(path):
    hashes = set()

    for dirpath, dirnames, filenames in os.walk(os.path.join(path, 'addons')):
        for filename in filenames:
            if (not filename.lower().endswith('.pbo')) and (not filename.lower().endswith('.ebo')):
                continue

            full_path = os.path.join(dirpath, filename)
            hash = get_pbo_sha1_hash(full_path)

            hashes.add(hash)

    return hashes


def order_hashes(unordered_hashes):
    hashes = [hash.decode('utf8') for hash in unordered_hashes]
    return [hash.encode('utf8') for hash in sorted(hashes, key=str.casefold)]


def get_longhash(hashes):
    ordered_hashes = order_hashes(hashes)
    m = hashlib.sha1()
    for hash in ordered_hashes:
        m.update(hash)

    longhash = m.hexdigest()
    return longhash


def get_shorthash(longhash):
    if isinstance(longhash, str):
        longhash = longhash.encode('utf8')

    to_hash = bytes([len(longhash) & 0xff]) + longhash
    return '{:08x}'.format(BIHash_bytes(to_hash))
