-- --
-- -- PostgreSQL database dump
-- --

-- -- Dumped from database version 10.5 (Debian 10.5-2.pgdg90+1)
-- -- Dumped by pg_dump version 11.5 (Ubuntu 11.5-1.pgdg18.04+1)

-- -- Started on 2019-08-14 17:08:11 IST

-- SET statement_timeout = 0;
-- SET lock_timeout = 0;
-- SET idle_in_transaction_session_timeout = 0;
-- SET client_encoding = 'UTF8';
-- SET standard_conforming_strings = on;
-- SELECT pg_catalog.set_config('search_path', '', false);
-- SET check_function_bodies = false;
-- SET xmloption = content;
-- SET client_min_messages = warning;
-- SET row_security = off;

-- SET default_tablespace = '';

-- SET default_with_oids = false;

-- --
-- -- TOC entry 198 (class 1259 OID 16392)
-- -- Name: metric1; Type: TABLE; Schema: public; Owner: admin_clixdata
-- --

-- CREATE TABLE public.metric1 (
--     id integer NOT NULL,
--     school_server_code character varying(64) NOT NULL,
--     date timestamp without time zone NOT NULL,
--     attendance_tools integer,
--     attendance_modules integer,
--     state character varying(32) NOT NULL,
--     district character varying(32) NOT NULL
-- );


-- ALTER TABLE public.metric1 OWNER TO admin_clixdata;

-- --
-- -- TOC entry 197 (class 1259 OID 16390)
-- -- Name: metric1_id_seq; Type: SEQUENCE; Schema: public; Owner: admin_clixdata
-- --

-- CREATE SEQUENCE public.metric1_id_seq
--     AS integer
--     START WITH 1
--     INCREMENT BY 1
--     NO MINVALUE
--     NO MAXVALUE
--     CACHE 1;


-- ALTER TABLE public.metric1_id_seq OWNER TO admin_clixdata;

-- --
-- -- TOC entry 2874 (class 0 OID 0)
-- -- Dependencies: 197
-- -- Name: metric1_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin_clixdata
-- --

-- ALTER SEQUENCE public.metric1_id_seq OWNED BY public.metric1.id;


-- --
-- -- TOC entry 2742 (class 2604 OID 16395)
-- -- Name: metric1 id; Type: DEFAULT; Schema: public; Owner: admin_clixdata
-- --

-- ALTER TABLE ONLY public.metric1 ALTER COLUMN id SET DEFAULT nextval('public.metric1_id_seq'::regclass);


-- --
-- -- TOC entry 2868 (class 0 OID 16392)
-- -- Dependencies: 198
-- -- Data for Name: metric1; Type: TABLE DATA; Schema: public; Owner: admin_clixdata
-- --

-- COPY public.metric1 (id, school_server_code, date, attendance_tools, attendance_modules, state, district) FROM stdin;
-- 1	2031016-mz16	2018-08-09 00:00:00	2	\N	mz	mz
-- 2	2031014-mz14	2018-10-24 00:00:00	26	\N	mz	mz
-- 3	2031004-mz4	2018-10-18 00:00:00	\N	27	mz	mz
-- 4	2031005-mz5	2018-08-07 00:00:00	\N	50	mz	mz
-- 5	2031005-mz5	2018-08-14 00:00:00	\N	29	mz	mz
-- 6	2031025-mz25	2018-10-05 00:00:00	\N	7	mz	mz
-- 7	2031025-mz25	2018-10-11 00:00:00	\N	13	mz	mz
-- 8	2031025-mz25	2018-10-31 00:00:00	\N	20	mz	mz
-- 9	2031025-mz25	2018-11-09 00:00:00	\N	15	mz	mz
-- 10	2031025-mz25	2018-11-21 00:00:00	\N	17	mz	mz
-- 11	2031030-mz30	2018-08-23 00:00:00	2	11	mz	mz
-- 12	2031030-mz30	2018-10-17 00:00:00	4	\N	mz	mz
-- 13	2031030-mz30	2018-10-18 00:00:00	25	17	mz	mz
-- 14	2031030-mz30	2018-10-24 00:00:00	4	\N	mz	mz
-- 15	2031030-mz30	2018-10-25 00:00:00	16	1	mz	mz
-- 16	2031030-mz30	2018-07-23 00:00:00	\N	7	mz	mz
-- 17	2031030-mz30	2018-08-16 00:00:00	\N	24	mz	mz
-- 18	2031030-mz30	2018-09-20 00:00:00	\N	68	mz	mz
-- 19	2031030-mz30	2018-10-04 00:00:00	\N	5	mz	mz
-- 20	2031030-mz30	2018-10-11 00:00:00	\N	26	mz	mz
-- 21	2031017-mz17	2018-08-16 00:00:00	2	19	mz	mz
-- 22	2031030-mz30	2018-08-23 00:00:00	2	11	mz	mz
-- 23	2031007-mz7	2018-08-24 00:00:00	1	1	mz	mz
-- 24	2031007-mz7	2018-09-10 00:00:00	1	1	mz	mz
-- 25	2031030-mz30	2018-10-17 00:00:00	4	\N	mz	mz
-- 26	2031030-mz30	2018-10-18 00:00:00	25	26	mz	mz
-- 27	2031030-mz30	2018-10-24 00:00:00	4	\N	mz	mz
-- 28	2031030-mz30	2018-10-25 00:00:00	16	1	mz	mz
-- 29	2031007-mz7	2018-08-13 00:00:00	\N	7	mz	mz
-- 30	2031007-mz7	2018-08-29 00:00:00	\N	1	mz	mz
-- 31	2031007-mz7	2018-08-30 00:00:00	\N	1	mz	mz
-- 32	2031007-mz7	2018-08-31 00:00:00	\N	1	mz	mz
-- 33	2031017-mz17	2018-08-14 00:00:00	\N	7	mz	mz
-- 34	2031017-mz17	2018-08-23 00:00:00	\N	17	mz	mz
-- 35	2031017-mz17	2018-10-08 00:00:00	\N	27	mz	mz
-- 36	2031017-mz17	2018-10-11 00:00:00	\N	40	mz	mz
-- 37	2031017-mz17	2018-10-12 00:00:00	\N	22	mz	mz
-- 38	2031017-mz17	2018-10-25 00:00:00	\N	20	mz	mz
-- 39	2031017-mz17	2018-10-26 00:00:00	\N	16	mz	mz
-- 40	2031017-mz17	2018-10-31 00:00:00	\N	18	mz	mz
-- 41	2031017-mz17	2018-11-13 00:00:00	\N	4	mz	mz
-- 42	2031017-mz17	2018-11-15 00:00:00	\N	8	mz	mz
-- 43	2031017-mz17	2018-11-20 00:00:00	\N	20	mz	mz
-- 44	2031017-mz17	2018-11-21 00:00:00	\N	5	mz	mz
-- 45	2031020-mz20	2018-08-10 00:00:00	\N	31	mz	mz
-- 46	2031020-mz20	2018-08-21 00:00:00	\N	20	mz	mz
-- 47	2031020-mz20	2018-08-28 00:00:00	\N	23	mz	mz
-- 48	2031020-mz20	2018-08-31 00:00:00	\N	21	mz	mz
-- 49	2031020-mz20	2018-10-09 00:00:00	\N	15	mz	mz
-- 50	2031020-mz20	2018-10-10 00:00:00	\N	8	mz	mz
-- 51	2031020-mz20	2018-10-26 00:00:00	\N	17	mz	mz
-- 52	2031020-mz20	2018-10-30 00:00:00	\N	18	mz	mz
-- 53	2031020-mz20	2018-10-31 00:00:00	\N	19	mz	mz
-- 54	2031020-mz20	2018-11-02 00:00:00	\N	17	mz	mz
-- 55	2031020-mz20	2018-11-09 00:00:00	\N	16	mz	mz
-- 56	2031020-mz20	2018-11-13 00:00:00	\N	18	mz	mz
-- 57	2031022-mz22	2018-08-13 00:00:00	\N	8	mz	mz
-- 58	2031022-mz22	2018-08-20 00:00:00	\N	36	mz	mz
-- 59	2031022-mz22	2018-09-14 00:00:00	\N	18	mz	mz
-- 60	2031030-mz30	2018-08-09 00:00:00	\N	7	mz	mz
-- 61	2031030-mz30	2018-08-16 00:00:00	\N	24	mz	mz
-- 62	2031030-mz30	2018-09-20 00:00:00	\N	68	mz	mz
-- 63	2031030-mz30	2018-10-04 00:00:00	\N	5	mz	mz
-- 64	2031030-mz30	2018-10-11 00:00:00	\N	26	mz	mz
-- \.


-- --
-- -- TOC entry 2875 (class 0 OID 0)
-- -- Dependencies: 197
-- -- Name: metric1_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_clixdata
-- --

-- SELECT pg_catalog.setval('public.metric1_id_seq', 64, true);


-- --
-- -- TOC entry 2745 (class 2606 OID 16397)
-- -- Name: metric1 metric1_pkey; Type: CONSTRAINT; Schema: public; Owner: admin_clixdata
-- --

-- ALTER TABLE ONLY public.metric1
--     ADD CONSTRAINT metric1_pkey PRIMARY KEY (id);


-- --
-- -- TOC entry 2743 (class 1259 OID 16398)
-- -- Name: ix_metric1_school_server_code; Type: INDEX; Schema: public; Owner: admin_clixdata
-- --

-- CREATE INDEX ix_metric1_school_server_code ON public.metric1 USING btree (school_server_code);


-- -- Completed on 2019-08-14 17:08:17 IST

-- --
-- -- PostgreSQL database dump complete
-- --

