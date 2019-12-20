def myaddarguments(parser):
#read filepath
    parser.add_argument("--mode", type=str, default="train_start",
                        help=("Software mode:"
                              "train_start for training from start,"
                              "train_continue for continue to train,"
                              "evaluate for test,"
                              "translate for instant translate."))
    parser.add_argument("--src", type=str, default=None,
                        help="Source suffix, e.g., en.")
    parser.add_argument("--tgt", type=str, default=None,
                        help="Target suffix, e.g., la.")
    parser.add_argument("--vocab_prefix", type=str, default=None, 
                        help="Vocab prefix, expect files with src/tgt suffixes.")
    parser.add_argument("--train_prefix", type=str, default=None,
                        help="Train prefix, expect files with src/tgt suffixes.")
    parser.add_argument("--test_prefix", type=str, default=None,
                        help="Test prefix, expect files with src/tgt suffixes.")
    parser.add_argument("--out_dir", type=str, default=None,
                        help="Store log/model files.")

#read hyper parameters
    parser.add_argument("--embedding_dim", type=int, default=64, 
                        help="Dimensions to embed the vocabulary into.")
    parser.add_argument("--num_units", type=int, default=128, help="Network size.")
    parser.add_argument("--batch", type=int, default=64,
                        help="Batch size of training data sentences.")
    parser.add_argument("--rate", type=float, default=0.001,
                        help="Learning rate of model.")
    parser.add_argument("--num_train_steps", type=int, default=2000,
                        help="Num steps to train.")
    parser.add_argument("--steps_per_stats", type=int, default=100,
                        help=("How many training steps to do per stats logging. "
                              "Save checkpoint every 10x steps_per_stats"))

def mycreateparams(myargs):
#passing hparams
    class hyperparameter:
        def __init__(self):
            self.mode = "train_start"
            self.src = ''
            self.tgt = ''
            self.vocab_prefix = ''
            self.train_prefix = ''
            self.test_prefix = ''
            self.out_dir = ''
            self.batch = 64
            self.train_data_size = 0
            self.src_vocab_size = 0
            self.tgt_vocab_size = 0
            self.max_input_length = 0
            self.max_output_length = 0
            self.embedding_dim = 64
            self.num_units = 128
            self.rate = 0.001
            self.num_train_steps = 2000
            self.steps_per_stats = 100
    hp = hyperparameter()
    hp.mode = myargs.mode
    hp.src = myargs.src
    hp.tgt = myargs.tgt
    hp.vocab_prefix = myargs.vocab_prefix
    hp.train_prefix = myargs.train_prefix
    hp.test_prefix = myargs.test_prefix
    hp.out_dir = myargs.out_dir
    hp.batch = myargs.batch
    hp.embedding_dim = myargs.embedding_dim
    hp.num_units = myargs.num_units
    hp.rate = myargs.rate
    hp.num_train_steps = myargs.num_train_steps
    hp.steps_per_stats = myargs.steps_per_stats
    return hp
