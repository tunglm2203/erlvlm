<div><h2>[ICML'25] Enhancing Rating-Based Reinforcement Learning to Effectively Leverage Feedback from Large Vision-Language Models</h2></div>
<br>

**Tung M. Luu, Younghwan Lee, Donghoon Lee, Sunho Kim,
Min Jun Kim, Chang D. Yoo**
<br>
KAIST, South Korea
<br>
[[Paper]](https://proceedings.mlr.press/v267/luu25a.html) [[Website]](https://erlvlm2025.github.io/) 


## Overview
This is the official implementation of **ERL-VLM** for MetaWorld tasks.

## Installation

```
conda create --name erlvlm python=3.9
conda activate erlvlm
pip install -r requirements.txt --no-deps
pip install -e .
```

## Setup Gemini Key:
1. Obtain a Gemini API key: Follow the instructions at https://aistudio.google.com/app/apikey
2. Enable parallel querying: We support querying Gemini in parallel using multiple keys, which can speed up the querying process. Place your API keys in `gemini_keys.py` and adjust parameters `n_processes_query` accordingly.

## Cached VLM rating labels
- We provide cached VLM rating labels collected during our experiments. Labels are saved only at VLM query steps (i.e., at fixed intervals during training).
- You can download the cached labels from this [Google Drive link](https://drive.google.com/drive/folders/1nL7PncAk98lPIpWDwzP57ypDb2jCY6gl?usp=sharing).
- After downloading, unzip the files to a directory of your choice and update the `CACHED_QUERY` path in the provided bash scripts accordingly.

## Run experiments
```
bash scripts/open_drawer/run_ERLVLM.sh
bash scripts/soccer/run_ERLVLM.sh
bash scripts/sweep_into/run_ERLVLM.sh
```

## Citation
If you use this repo in your research, please consider citing the paper as follows:
```
@inproceedings{
    luu2025enhancing,
    title={Enhancing Rating-Based Reinforcement Learning to Effectively Leverage Feedback from Large Vision-Language Models},
    author={Tung Minh Luu and Younghwan Lee and Donghoon Lee and Sunho Kim and Min Jun Kim and Chang D. Yoo},
    booktitle={Forty-second International Conference on Machine Learning},
    year={2025},
    url={https://openreview.net/forum?id=k77bq8AJVy}
}
```

## Acknowledgements
- This work was supported by Institute for Information & communications Technology Planning & Evaluation (IITP) grant funded by the Korea government(MSIT) (No.RS2021-II211381, Development of Causal AI through Video Understanding and Reinforcement Learning, and Its Applications to Real Environments) and partly supported by Institute of Information & communications Technology Planning & Evaluation (IITP) grant funded by the Korea government(MSIT) (No.RS-2022-II220184, Development and Study of AI Technologies to Inexpensively Conform to Evolving Policy on Ethics).

- This repo contains code adapted from [RbRL](https://github.com/Dev1nW/Rating-based-Reinforcement-Learning), 
[RL-VLM-F](https://github.com/yufeiwang63/RL-VLM-F). We thank the authors and contributors for open-sourcing their code.

## License

MIT
