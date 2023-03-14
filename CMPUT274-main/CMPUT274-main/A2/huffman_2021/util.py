import bitio
import huffman
import pickle
import operator


def read_tree(tree_stream):
  
  with open(tree_stream, 'rb') as fin:
    tree = pickle.load(fin)

  return tree
    
  '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream to read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
  '''


def decode_byte(tree, bitreader):
  
  #if bitreader.isinstance(TreeLeaf):
   # return tree.getValue()

  #else:
   # if bitreader.tree.left:
    #  return decode_byte(tree.getLeft(), bitreader)
    #elif bitreader.tree.right:
     # return decode_byte(tree.getRight(), bitreader)

   '''
   Don't know which one will work, just gonna filp the coin
   '''   


  while not bitreader.isinstance(TreeLeaf):
    bitreader.readbit()

    if bitreader.tree.left:
      tree.getLeft()
    elif bitreader.tree.right:
      tree.getRight()

    return tree.getValue()


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



def decompress(compressed, uncompressed):
  
  tree = read_tree(compressed)
  bits = bitio.BitReader.readbit()

  uncompressed

  if compressed.tree.TreeLeaf:
    a = uncompressed.tree.getValue()
    uncompressed.write(a)






  '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
  '''


def write_tree(tree, tree_stream):
  
  with open(tree_stream, 'wb') as fout:
    new_tree = pickle.dump(tree, fout)

    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''


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
