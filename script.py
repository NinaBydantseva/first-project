-- public.user_activity_log definition

-- Drop table

-- DROP TABLE public.user_activity_log;

CREATE TABLE public.user_activity_log (
	id serial4 NOT NULL,
	client_id int8 NOT NULL, -- id of our clients
	hitdatetime timestamp NULL, -- timestamp when client make some action in our company ux
	"action" varchar(20) NULL -- action name what client done at hitdatetime moment
);

-- Column comments

COMMENT ON COLUMN public.user_activity_log.client_id IS 'id of our clients';
COMMENT ON COLUMN public.user_activity_log.hitdatetime IS 'timestamp when client make some action in our company ux';
COMMENT ON COLUMN public.user_activity_log."action" IS 'action name what client done at hitdatetime moment';

-- Permissions

ALTER TABLE public.user_activity_log OWNER TO de_ninabydantseva;
GRANT ALL ON TABLE public.user_activity_log TO de_ninabydantseva;


-- public.user_attributes definition

-- Drop table

-- DROP TABLE public.user_attributes;

CREATE TABLE public.user_attributes (

);

-- Permissions

ALTER TABLE public.user_attributes OWNER TO de_ninabydantseva;
GRANT ALL ON TABLE public.user_attributes TO de_ninabydantseva;


-- public.user_payment_log definition

-- Drop table

-- DROP TABLE public.user_payment_log;

CREATE TABLE public.user_payment_log (

);

-- Permissions

ALTER TABLE public.user_payment_log OWNER TO de_ninabydantseva;
GRANT ALL ON TABLE public.user_payment_log TO de_ninabydantseva;