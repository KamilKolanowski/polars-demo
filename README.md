# Polars Demo

This project demonstrates **Polars**, a modern DataFrame library designed for high-performance data processing in Python and Rust. The goal is to showcase what Polars is, why it exists, how it works in practice, and how it compares to Apache Spark in common data processing scenarios.

---

## What is Polars?

**Polars** is a fast, memory-efficient DataFrame library built on top of **Apache Arrow**. It is implemented in Rust with Python bindings and is designed to efficiently handle analytical workloads on a **single machine**.

Unlike traditional row-based DataFrame libraries, Polars uses a **columnar memory model** and a **lazy execution engine**, allowing it to optimize queries before execution.

---

## Key Features of Polars

- **Columnar execution (Apache Arrow)**
  - Efficient CPU cache usage
  - Zero-copy data sharing with other Arrow-based systems

- **Lazy evaluation**
  - Query plans are optimized before execution
  - Predicate pushdown, projection pruning, and query reordering

- **Multi-threaded by default**
  - Automatically uses all available CPU cores
  - No explicit parallelization required

- **Low memory footprint**
  - Suitable for large datasets on a single machine
  - Avoids JVM overhead

- **Pythonic API**
  - Familiar to users of pandas
  - Expression-based transformations

---

## Simple Example: Polars vs Spark

### Example Task
Filter trips longer than 10 km and compute average duration.

---

### Polars (Lazy API)

```python
import polars as pl

df = pl.scan_csv("trips.csv")

result = (
    df.filter(pl.col("distance") > 10)
      .select(pl.col("duration").mean())
)

result.collect()
```

What happens internally:
- The query is not executed immediately
- Polars builds an optimized execution plan
- Only required columns are read from disk
- The computation is parallelized automatically

### Spark (PySpark)

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("trips.csv", header=True, inferSchema=True)

result = (
    df.filter(col("distance") > 10)
      .select(avg("duration"))
)

result.show()
```

What happens internally:
- A distributed execution plan is created
- Data may be shuffled across executors
- JVM-based execution with higher overhead

___

| Aspect            | Polars                         | Spark                          |
|------------------|--------------------------------|--------------------------------|
| Execution model   | Single-node, multi-threaded    | Distributed (cluster-based)    |
| Language core     | Rust                           | JVM (Scala/Java)               |
| Memory model      | Apache Arrow (columnar)        | JVM objects + Tungsten         |
| Setup complexity  | Minimal                        | High (cluster, configs)        |
| Latency           | Very low                       | Higher                         |
| Scalability       | Vertical (scale-up)            | Horizontal (scale-out)         |

___

### Polars is the better choice when:
- Data fits on a single machine
- You need fast local analytics
- You want low latency (seconds, not minutes)
- You are replacing or extending pandas
- You want simple deployment without cluster management

### Typical use cases:
- Local analytics and feature engineering
- ETL jobs on medium-to-large datasets
- Data science workflows
- Streaming micro-batch processing on one node
___

### Spark is the better choice when:
- Data does not fit on a single machine
- You require horizontal scalability
- You already operate a Spark ecosystem
- You need tight integration with Hadoop, Hive, or HDFS

### Typical use cases:
- Massive datasets (TB+)
- Distributed joins across many sources
- Enterprise-scale batch pipelines
- Shared compute clusters
___


# Summary
- Polars and Spark are not competitors in all scenarios—they solve different problems:
- Polars excels at fast, efficient, single-node analytics with minimal overhead.
- Spark excels at distributed processing at very large scale.
- This project focuses on demonstrating how Polars can often replace Spark or pandas for many analytical workloads while providing simpler code, faster execution, and lower operational cost.
