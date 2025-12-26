#!/bin/bash

GPU_ID=0

ENV_NAME="metaworld_soccer-v2"

CACHED_QUERY="path_to_your_query_cached"

WANDB_GROUP="erlvlm_${ENV_NAME}"

CUDA_VISIBLE_DEVICES=$GPU_ID python train_PEBBLE_VLM.py \
  env=$ENV_NAME \
  num_unsup_steps=9000 num_train_steps=1000000 \
  num_ratings=2 \
  image_reward=True \
  vlm_feedback=True \
  reward_loss="mae" \
  weighting_loss=True \
  batch_stratify=True \
  run_group=$WANDB_GROUP \
  n_processes_query=5 \
  use_cached=True \
  query_cached=$CACHED_QUERY \
  seed=1 \
  debug=False
