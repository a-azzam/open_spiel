
from absl import app
from absl import flags
from absl import logging

from open_spiel.python.algorithms import generate_playthrough

FLAGS = flags.FLAGS

flags.DEFINE_string(
    "game", "kuhn_poker", "Name of the game, with optional parameters, e.g. "
    "'kuhn_poker' or 'go(komi=4.5,board_size=19)'.")
flags.DEFINE_string("output_file", None, "Where to write the data to.")
flags.DEFINE_list("actions", None,
                  "A (possibly partial) list of action choices to make.")

flags.DEFINE_string("update_path", None,
                    "If set, regenerates all playthroughs in the path.")
flags.DEFINE_bool(
    "alsologtostdout", False,
    "If True, the trace will be written to std-out while it "
    "is being constructed (in addition to the usual behavior).")
flags.DEFINE_integer("shard", 0, "The shard to update.")
flags.DEFINE_integer("num_shards", 1, "How many shards to use for updates.")


def main(unused_argv):
  actions = FLAGS.actions
  if actions is not None:
    actions = [int(x) for x in actions]

  text = generate_playthrough.playthrough(
      "python_dynamic_routing", actions, alsologtostdout=FLAGS.alsologtostdout)
  with open('/home/azzam/thesis/open_spiel/open_spiel/logs/dynamic_routing.txt', "w") as f:
    f.write(text)

  text_mfg = generate_playthrough.playthrough(
      "python_mfg_dynamic_routing", actions, alsologtostdout=FLAGS.alsologtostdout)
  with open('/home/azzam/thesis/open_spiel/open_spiel/logs/dynamic_mfg_routing.txt', "w") as f:
    f.write(text_mfg)

  text_mfc = generate_playthrough.playthrough(
      "python_mfc_dynamic_routing", actions, alsologtostdout=FLAGS.alsologtostdout)
  with open('/home/azzam/thesis/open_spiel/open_spiel/logs/dynamic_mfc_routing.txt', "w") as f:
    f.write(text_mfc)

if __name__ == "__main__":
  app.run(main)
