drop table if exists tasks;
create table tasks (
	task_id integer primary key autoincrement,
	task varchar(22) NOT NULL,
	date date NOT NULL,
	starttime time,
	endtime time
	);
