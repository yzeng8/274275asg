import bitio
import huffman
import pickle
import operator


def read_tree(tree_stream):
  tree = pickle.load(tree_stream)

  return tree
    
  '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream to read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
  '''
  pass

def decode_byte(tree, bitreader):
    
  if isinstance(tree, huffman.TreeLeaf):
    return tree.getValue()

  bitValue = bitreader.readbit()
  
  if bitValue == False:
    return decode_byte(tree.getLeft(), bitreader)
  else:
    return decode_byte(tree.getRight(), bitreader)

  return tree.getValue()

#  if bitreader.isinstance(TreeLeaf):
#    return tree.getValue()
#
#  else:
#    if bitreader.tree.left:
#      return decode_byte(tree.getLeft(), bitreader)
#    elif bitreader.tree.right:
#      return decode_byte(tree.getRight(), bitreader)

#   '''
#   Don't know which one will work, just gonna filp the coin
#   '''   


#  while not bitreader.isinstance(TreeLeaf):
#    
#    bitValue = bitreader.readbit()
#
#    if (bitValue==0 && bitreader.tree.left):
#      tree.getLeft()
#    elif (bitValue==1 &&  bitreader.tree.right):
#      tree.getRight()
#
#  return tree.getValue()


#    """
#    Reads bits from the bit reader and traverses the tree from
#    the root to a leaf. Once a leaf is reached, bits are no longer read
#    and the value of that leaf is returned.

#    Args:
#      bitreader: An instance of bitio.BitReader to read the tree from.
#      tree: A Huffman tree.
#
#    Returns:
#      Next byte of the compressed bit stream.
#    """




def decompress(compressed, uncompressed):
  
  tree = read_tree(compressed)

  bitreader = bitio.BitReader(compressed)
  bitwriter = bitio.BitWriter(uncompressed)
    
  while True:
    try:
        byte_decoded = decode_byte(tree, bitreader)
        
        if type(byte_decoded) is type(None):
            bitwriter.flush()
            break
            
        bitwriter.writebits(byte_decoded, 8)
        
    except EOFError:
        bitwriter.flush()
        break



  # '''First, read a Huffman tree from the 'compressed' stream using your
    # read_tree function. Then use that tree to decode the rest of the
    # stream and write the resulting symbols to the 'uncompressed'
    # stream.

    # Args:
      # compressed: A file stream from which compressed input is read.
      # uncompressed: A writable file stream to which the uncompressed
          # output is written.
  # '''


def write_tree(tree, tree_stream):
  
    new_tree = pickle.dump(tree, tree_stream)

    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''


def compress(tree, uncompressed, compressed):

  #get the table
  table = huffman.make_encoding_table(tree)
  
  #write tree to compressed
  write_tree(tree, compressed)
  
  ##get the bit reader and writer
  bitreader = bitio.BitReader(uncompressed)
  bitwriter = bitio.BitWriter(compressed)
    
  while True:
    try:
        byte_uncompressed = bitreader.readbits(8)
        bits_to_write = table[byte_uncompressed]     
        
        for bit_each in bits_to_write:
          bitwriter.writebit(bit_each)

    except EOFError:
        for bit_each in table[None]:
          bitwriter.writebit(bit_each)

        bitwriter.flush()
        break

