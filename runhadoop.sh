# delete results on hadoop cluster
hdfs dfs -rm -r assignment-docs/results

# delete results locally
rm -rf results/

# run hadoop command
hadoop jar /home/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-D mapred.reduce.tasks=2 \
-files mapper.py,reducer.py,combiner.py,years.txt,genres.txt \
-mapper mapper.py \
-reducer reducer.py \
-combiner combiner.py \
-input /user/rkw00013/assignment-docs/ratings.txt \
-output /user/rkw00013/assignment-docs/results

# download results
hdfs dfs -copyToLocal assignment-docs/results results
