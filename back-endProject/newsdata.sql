--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: articles; Type: TABLE; Schema: public; Owner: vagrant; Tablespace:
--

CREATE TABLE articles (
    author integer NOT NULL,
    title text NOT NULL,
    slug text NOT NULL,
    lead text,
    body text,
    "time" timestamp with time zone DEFAULT now(),
    id integer NOT NULL
);


ALTER TABLE articles OWNER TO vagrant;

--
-- Name: articles_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE articles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE articles_id_seq OWNER TO vagrant;

--
-- Name: articles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE articles_id_seq OWNED BY articles.id;


--
-- Name: authors; Type: TABLE; Schema: public; Owner: vagrant; Tablespace:
--

CREATE TABLE authors (
    name text NOT NULL,
    bio text,
    id integer NOT NULL
);


ALTER TABLE authors OWNER TO vagrant;

--
-- Name: authors_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE authors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE authors_id_seq OWNER TO vagrant;

--
-- Name: authors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE authors_id_seq OWNED BY authors.id;


--
-- Name: log; Type: TABLE; Schema: public; Owner: vagrant; Tablespace:
--

CREATE TABLE log (
    path text,
    ip inet,
    method text,
    status text,
    "time" timestamp with time zone DEFAULT now(),
    id integer NOT NULL
);


ALTER TABLE log OWNER TO vagrant;

--
-- Name: log_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE log_id_seq OWNER TO vagrant;

--
-- Name: log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE log_id_seq OWNED BY log.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY articles ALTER COLUMN id SET DEFAULT nextval('articles_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY authors ALTER COLUMN id SET DEFAULT nextval('authors_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY log ALTER COLUMN id SET DEFAULT nextval('log_id_seq'::regclass);


--
-- Data for Name: articles; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY articles (author, title, slug, lead, body, "time", id) FROM stdin;
3	Bad things gone, say good people	bad-things-gone	All bad things have gone away, according to a poll of good people Thursday.	Bad things are a thing of the bad, bad past. Or so say good people, who were asked by pollsters Thursday whether bad things still are.	2016-08-15 11:55:10.814316-07	23
4	Balloon goons doomed	balloon-goons-doomed	The doom of balloon goons is true news.	The goons are doomed, no matter how much their balloons balloon.	2016-08-15 11:55:10.814316-07	24
1	Bears love berries, alleges bear	bears-love-berries	Rumors that bears love berries were confirmed by bear, who also proclaims love of salmon and honey.	Bear specified that raspberries were a personal favorite, although wild blackberries remain more abundant throughout the summer and early fall.	2016-08-15 11:55:10.814316-07	25
2	Candidate is jerk, alleges rival	candidate-is-jerk	That political candidate is a real jerk, according to a rival.	The rival alleged egotism, arrogance, and an almost fanatical devotion to media grandstanding. The candidate's campaign denied everything, and retaliated that the rival is a doo-doo head.	2016-08-15 11:55:10.814316-07	26
1	Goats eat Google's lawn	goats-eat-googles	A herd of goats are eating Google's lawn.	And the Googlers think it's super cute.	2016-08-15 11:55:10.814316-07	27
1	Media obsessed with bears	media-obsessed-with-bears	Media sources claim media figures fixated on bears and bear-related products.	Traditional media prefer green bears while online reporters love polar bears.	2016-08-15 11:55:10.814316-07	28
2	Trouble for troubled troublemakers	trouble-for-troubled	Troublemakers with troubles are in trouble, allege trouble consultants.	Four out of five troublemakers have trouble with trouble, according to a troubling study published Tuesday by the Troubled Troublemakers Project.	2016-08-15 11:55:10.814316-07	30
1	There are a lot of bears	so-many-bears	There certainly are a lot of bears in these woods.	My goodness, there really are very many bears. There are brown bears, black bears, green bears, and pink bears. No, wait, I think some of the green bears are actually trees. Trees are a lot like bears, in that they live in the woods and have very sharp teeth.	2016-08-15 11:55:10.814316-07	29
\.


--
-- Name: articles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('articles_id_seq', 30, true);


--
-- Data for Name: authors; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY authors (name, bio, id) FROM stdin;
Ursula La Multa	Ursula La Multa is an expert on bears, bear abundance, and bear accessories.	1
Rudolf von Treppenwitz	Rudolf von Treppenwitz is a nonprofitable disorganizer specializing in procrastinatory operations.	2
Anonymous Contributor	Anonymous Contributor's parents had unusual taste in names.	3
Markoff Chaney	Markoff Chaney is the product of random genetics.	4
\.


--
-- Name: authors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('authors_id_seq', 4, true);


--
-- Data for Name: log; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY log (path, ip, method, status, "time", id) FROM stdin;
