"""
  Compressing GANs using Knowledge Distillation.
  Teacher GAN: ESRGAN (https://github.com/captain-pool/E2_ESRGAN)

Citation:
  @article{DBLP:journals/corr/abs-1902-00159,
    author    = {Angeline Aguinaldo and
    Ping{-}Yeh Chiang and
    Alexander Gain and
    Ameya Patil and
    Kolten Pearson and
    Soheil Feizi},
    title     = {Compressing GANs using Knowledge Distillation},
    journal   = {CoRR},
    volume    = {abs/1902.00159},
    year      = {2019},
    url       = {http://arxiv.org/abs/1902.00159},
    archivePrefix = {arXiv},
    eprint    = {1902.00159},
    timestamp = {Tue, 21 May 2019 18:03:39 +0200},
    biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1902-00159},
    bibsource = {dblp computer science bibliography, https://dblp.org}
  }
"""
from absl import logging
import argparse
from libs.models import teacher
from libs import model
from libs import train
from libs import settings
import tensorflow as tf


def train_and_export(**kwargs):
  student_settings = settings.Settings(kwargs["config"], student=True)
  teacher_settings = settings.Settings(
      student_settings["teacher_config"], student=False)
  stats = settings.Stats(os.path.join(student_settings.path, "stats.yaml"))
  summary_writer = tf.summmary.create_file_writer(kwargs["logdir"])

  student_generator = model.Registry[student_settings["student_network"]]()
  teacher_generator = teacher.generator(out_channel=3)
  teacher_discriminator = teacher.discriminator()

  trainer = train.Trainer(
      teacher_generator,
      teacher_discriminator,
      summary_writer,
      data_dir=kwargs["datadir"],
      manual=kwargs["manual"],
      model_dir=kwargs["modeldir"])
  if kwargs["type"].lower().startswith("comparative"):
    trainer.train_comparative(student_generator)
    stats["type"] = "comparative"
    stats["trained"] = True
  elif kwargs["type"].lower().startswith("adversarial"):
    trainer.train_adversarial(student_generator)
    stats["type"] = "adversarial"
    stats["trained"] = True

  tf.saved_model.save(
      student_generator,
      os.path.join(
          kwargs["modeldir"],
          "compressed_esrgan"))


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--logdir", default=None, help="Path to log directory")
  parser.add_argument(
      "--config",
      default="config/config.yaml",
      help="path to config file")
  parser.add_argument(
      "--datadir",
      default=None,
      help="Path to custom data directory")
  parser.add_argument(
      "--manual",
      default=False,
      action="store_true",
      help="Specify if datadir stores files instead of TFRecords")
  parser.add_argument(
      "--modeldir",
      default=None,
      help="directory to store checkpoints and SavedModel")
  parser.add_argument(
      "--type",
      default=None,
      help="Train Student 'adversarial'-ly / 'comparative'-ly")
  parser.add_argument(
      "--verbose",
      "-v",
      default=0,
      action="count",
      help="Increases Verbosity. Repeat to increase more")

  FLAGS, unparsed = parser.parse_known_args()
  log_levels = [logging.WARNING, logging.INFO, logging.DEBUG]
  log_level = log_levels[min(FLAGS.verbose, len(log_levels) - 1)]
  logging.set_verbosity(log_level)
  train_and_export(**vars(FLAGS))