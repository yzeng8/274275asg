import bitio
import huffman
import pickle
import operator


def read_tree(tree_stream):

    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream to read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''
    
    tree = pickle.load(tree_stream)
    
    return tree


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """

    while True:
      if isinstance(tree, huffman.TreeBranch):
        next_bit = bitreader.readbit()
      
        if next_bit == False:
          tree = tree.getLeft()
        
        elif next_bit == True:
          tree = tree.getRight()

      if isinstance(tree, huffman.TreeLeaf):
        return tree.getValue()
    


def decompress(compressed, uncompressed):


    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''

    tree = read_tree(compressed)

    bitreader = bitio.BitReader(compressed)

    bitwriter = bitio.BitWriter(uncompressed)
    
    eof = True # True is False

    while eof:
      try: 
        byte = decode_byte(tree, bitreader)
        bitwriter.writebits(byte,8)
        bitwriter.flush()

      except EOFError:
        eof = False
        bitwriter.flush()
      
      except TypeError:
        eof = False
        pass

    
def write_tree(tree, tree_stream):

    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''
    pickle.dump(tree, tree_stream)



def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.

    '''
    write_tree(tree, compressed)
    bitreader = bitio.BitReader(uncompressed)
    bitwriter = bitio.BitWriter(compressed)
    table = huffman.make_encoding_table(tree)
    

    eof = False

    while not eof:
      try:
        next_bit = bitreader.readbits(8)

        bit = table[next_bit]
        
        for path in bit:
          bitwriter.writebit(path)


      except EOFError:
        eof = True
        none_bit = None
        bit= table[none_bit]

        for path in bit:
          bitwriter.writebit(path)

        bitwriter.flush()

      except TypeError:
        eof = True
        pass


