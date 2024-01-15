# Running script for the 8m shuffled traces on 11th January

python3 /mnt/sdb/cornflakes/experiments/zcc-cf-kv-bench.py \
-e individual \
-f /mnt/sdb/results \
-c /mnt/sdb/cornflakes/vish_config.yaml \
-ec /mnt/sdb/cornflakes/experiments/yamls/cmdlines/0cc/0cc-ycsb.yaml \
-lt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.load \
-qt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.access \
-nc 1 --num_threads 16 \
--rate 6250 \
--size 2048 \
--num_keys 1 --num_values 1 \
--system vanilla_cornflakes \
--zcc_pinning_budget 1024 \
--zcc_segment_size 64 \
--pprint

# Server side

sudo env LD_LIBRARY_PATH=/mnt/sdb/cornflakes/dpdk-datapath/3rdparty/dpdk/build/lib/x86_64-linux-gnu nice -n -19 taskset -c 2 /mnt/sdb/cornflakes/target/release/ycsb_mlx5 --config_file /mnt/sdb/cornflakes/vish_config.yaml --server_ip 10.10.1.1 --mode server --trace /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.load --debug_level info --value_size UniformOverSizes-2048 --num_values 1 --num_keys 1 --serialization cornflakes-dynamic --push_buf_type hybridarenaobject --inline_mode nothing --copy_threshold 512 --use_linked_list --num_pages 64 --zcc_pinning_limit 64000 --zcc_segment_size 64 --zcc_alg noalg --zcc_sleep_duration 1000

# Client side

sudo env LD_LIBRARY_PATH=/mnt/sdb/cornflakes/dpdk-datapath/3rdparty/dpdk/build/lib/x86_64-linux-gnu /mnt/sdb/cornflakes/target/release/ycsb_dpdk --config_file /mnt/sdb/cornflakes/vish_config.yaml --mode client --queries /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.access --debug_level debug --push_buf_type singlebuf --value_size UniformOverSizes-2048 --rate 100 --serialization cornflakes1c-dynamic --server_ip 10.10.1.1 --our_ip 10.10.1.2 --time 25 --num_values 1 --num_keys 1 --num_threads 16 --num_clients 1 --client_id 0 --use_linked_list


# Segment size 16 

nohup python3 /mnt/sdb/cornflakes/experiments/zcc-cf-kv-bench.py \
-e loop \
-f /mnt/sdb/looping_params_ss16_results \
-c /mnt/sdb/cornflakes/vish_config.yaml \
-ec /mnt/sdb/cornflakes/experiments/yamls/cmdlines/0cc/0cc-ycsb.yaml \
-lt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.load \
-qt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.access \
-lc /mnt/sdb/cornflakes/experiments/yamls/loopingparams/0cc/0cc-synthetic-16.yaml &

# Segment size 32

nohup python3 /mnt/sdb/cornflakes/experiments/zcc-cf-kv-bench.py \
-e loop \
-f /mnt/sdb/looping_params_ss32_results_3 \
-c /mnt/sdb/cornflakes/vish_config.yaml \
-ec /mnt/sdb/cornflakes/experiments/yamls/cmdlines/0cc/0cc-ycsb.yaml \
-lt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.load \
-qt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.access \
-lc /mnt/sdb/cornflakes/experiments/yamls/loopingparams/0cc/0cc-synthetic-32.yaml &

# Segment size 64

nohup python3 /mnt/sdb/cornflakes/experiments/zcc-cf-kv-bench.py \
-e loop \
-f /mnt/sdb/looping_params_ss64_results \
-c /mnt/sdb/cornflakes/vish_config.yaml \
-ec /mnt/sdb/cornflakes/experiments/yamls/cmdlines/0cc/0cc-ycsb.yaml \
-lt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.load \
-qt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.access \
-lc /mnt/sdb/cornflakes/experiments/yamls/loopingparams/0cc/0cc-synthetic-64.yaml &

# Segment size 128

nohup python3 /mnt/sdb/cornflakes/experiments/zcc-cf-kv-bench.py \
-e loop \
-f /mnt/sdb/looping_params_ss128_results \
-c /mnt/sdb/cornflakes/vish_config.yaml \
-ec /mnt/sdb/cornflakes/experiments/yamls/cmdlines/0cc/0cc-ycsb.yaml \
-lt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.load \
-qt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.access \
-lc /mnt/sdb/cornflakes/experiments/yamls/loopingparams/0cc/0cc-synthetic-128.yaml &


# Segment size 256

nohup python3 /mnt/sdb/cornflakes/experiments/zcc-cf-kv-bench.py \
-e loop \
-f /mnt/sdb/looping_params_ss256_results \
-c /mnt/sdb/cornflakes/vish_config.yaml \
-ec /mnt/sdb/cornflakes/experiments/yamls/cmdlines/0cc/0cc-ycsb.yaml \
-lt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.load \
-qt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.access \
-lc /mnt/sdb/cornflakes/experiments/yamls/loopingparams/0cc/0cc-synthetic-256.yaml &

# Segment size 256

nohup python3 /mnt/sdb/cornflakes/experiments/zcc-cf-kv-bench.py \
-e loop \
-f /mnt/sdb/looping_params_ss512_results \
-c /mnt/sdb/cornflakes/vish_config.yaml \
-ec /mnt/sdb/cornflakes/experiments/yamls/cmdlines/0cc/0cc-ycsb.yaml \
-lt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.load \
-qt /mnt/sdb/8m_workload/workload_8m_shuffled-1-batched.access \
-lc /mnt/sdb/cornflakes/experiments/yamls/loopingparams/0cc/0cc-synthetic-512.yaml &