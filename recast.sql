BEGIN;
--
-- Create model Actor
--
CREATE TABLE "recast_actor" ("id" bigserial NOT NULL PRIMARY KEY, "tmdbid" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "img" varchar(500) NOT NULL);
--
-- Create model Movie
--
CREATE TABLE "recast_movie" ("id" bigserial NOT NULL PRIMARY KEY, "tmbid" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "img" varchar(500) NOT NULL);
--
-- Create model Recast
--
CREATE TABLE "recast_recast" ("id" bigserial NOT NULL PRIMARY KEY, "name" varchar(255) NOT NULL, "desc" text NOT NULL);
--
-- Create model User
--
CREATE TABLE "recast_user" ("id" bigserial NOT NULL PRIMARY KEY, "name" varchar(255) NOT NULL, "password" varchar(255) NOT NULL);
--
-- Create model RecastInst
--
CREATE TABLE "recast_recastinst" ("id" bigserial NOT NULL PRIMARY KEY, "name" varchar(255) NOT NULL, "actor_id" bigint NULL, "recast_id" bigint NOT NULL);
CREATE TABLE "recast_recastinst_downvotes" ("id" bigserial NOT NULL PRIMARY KEY, "recastinst_id" bigint NOT NULL, "user_id" bigint NOT NULL);
CREATE TABLE "recast_recastinst_upvotes" ("id" bigserial NOT NULL PRIMARY KEY, "recastinst_id" bigint NOT NULL, "user_id" bigint NOT NULL);
--
-- Add field downvotes to recast
--
CREATE TABLE "recast_recast_downvotes" ("id" bigserial NOT NULL PRIMARY KEY, "recast_id" bigint NOT NULL, "user_id" bigint NOT NULL);
--
-- Add field movie to recast
--
ALTER TABLE "recast_recast" ADD COLUMN "movie_id" bigint NULL CONSTRAINT "recast_recast_movie_id_4a7a2552_fk_recast_movie_id" REFERENCES "recast_movie"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "recast_recast_movie_id_4a7a2552_fk_recast_movie_id" IMMEDIATE;
--
-- Add field upvotes to recast
--
CREATE TABLE "recast_recast_upvotes" ("id" bigserial NOT NULL PRIMARY KEY, "recast_id" bigint NOT NULL, "user_id" bigint NOT NULL);
--
-- Add field user to recast
--
ALTER TABLE "recast_recast" ADD COLUMN "user_id" bigint NULL CONSTRAINT "recast_recast_user_id_79fe6d86_fk_recast_user_id" REFERENCES "recast_user"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "recast_recast_user_id_79fe6d86_fk_recast_user_id" IMMEDIATE;
--
-- Create model CastInst
--
CREATE TABLE "recast_castinst" ("id" bigserial NOT NULL PRIMARY KEY, "name" varchar(255) NOT NULL, "actor_id" bigint NULL, "movie_id" bigint NOT NULL);
ALTER TABLE "recast_recastinst" ADD CONSTRAINT "recast_recastinst_actor_id_e667f3bd_fk_recast_actor_id" FOREIGN KEY ("actor_id") REFERENCES "recast_actor" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "recast_recastinst" ADD CONSTRAINT "recast_recastinst_recast_id_1710e072_fk_recast_recast_id" FOREIGN KEY ("recast_id") REFERENCES "recast_recast" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "recast_recastinst_actor_id_e667f3bd" ON "recast_recastinst" ("actor_id");
CREATE INDEX "recast_recastinst_recast_id_1710e072" ON "recast_recastinst" ("recast_id");
ALTER TABLE "recast_recastinst_downvotes" ADD CONSTRAINT "recast_recastinst_downvotes_recastinst_id_user_id_098e3a41_uniq" UNIQUE ("recastinst_id", "user_id");
ALTER TABLE "recast_recastinst_downvotes" ADD CONSTRAINT "recast_recastinst_do_recastinst_id_5d2676d2_fk_recast_re" FOREIGN KEY ("recastinst_id") REFERENCES "recast_recastinst" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "recast_recastinst_downvotes" ADD CONSTRAINT "recast_recastinst_downvotes_user_id_f3410f5a_fk_recast_user_id" FOREIGN KEY ("user_id") REFERENCES "recast_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "recast_recastinst_downvotes_recastinst_id_5d2676d2" ON "recast_recastinst_downvotes" ("recastinst_id");
CREATE INDEX "recast_recastinst_downvotes_user_id_f3410f5a" ON "recast_recastinst_downvotes" ("user_id");
ALTER TABLE "recast_recastinst_upvotes" ADD CONSTRAINT "recast_recastinst_upvotes_recastinst_id_user_id_cc143987_uniq" UNIQUE ("recastinst_id", "user_id");
ALTER TABLE "recast_recastinst_upvotes" ADD CONSTRAINT "recast_recastinst_up_recastinst_id_f8403ff1_fk_recast_re" FOREIGN KEY ("recastinst_id") REFERENCES "recast_recastinst" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "recast_recastinst_upvotes" ADD CONSTRAINT "recast_recastinst_upvotes_user_id_c3922d5f_fk_recast_user_id" FOREIGN KEY ("user_id") REFERENCES "recast_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "recast_recastinst_upvotes_recastinst_id_f8403ff1" ON "recast_recastinst_upvotes" ("recastinst_id");
CREATE INDEX "recast_recastinst_upvotes_user_id_c3922d5f" ON "recast_recastinst_upvotes" ("user_id");
ALTER TABLE "recast_recast_downvotes" ADD CONSTRAINT "recast_recast_downvotes_recast_id_user_id_7a8d78d2_uniq" UNIQUE ("recast_id", "user_id");
ALTER TABLE "recast_recast_downvotes" ADD CONSTRAINT "recast_recast_downvotes_recast_id_38725f88_fk_recast_recast_id" FOREIGN KEY ("recast_id") REFERENCES "recast_recast" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "recast_recast_downvotes" ADD CONSTRAINT "recast_recast_downvotes_user_id_fbe1be33_fk_recast_user_id" FOREIGN KEY ("user_id") REFERENCES "recast_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "recast_recast_downvotes_recast_id_38725f88" ON "recast_recast_downvotes" ("recast_id");
CREATE INDEX "recast_recast_downvotes_user_id_fbe1be33" ON "recast_recast_downvotes" ("user_id");
CREATE INDEX "recast_recast_movie_id_4a7a2552" ON "recast_recast" ("movie_id");
ALTER TABLE "recast_recast_upvotes" ADD CONSTRAINT "recast_recast_upvotes_recast_id_user_id_d2cf6029_uniq" UNIQUE ("recast_id", "user_id");
ALTER TABLE "recast_recast_upvotes" ADD CONSTRAINT "recast_recast_upvotes_recast_id_cd3ca601_fk_recast_recast_id" FOREIGN KEY ("recast_id") REFERENCES "recast_recast" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "recast_recast_upvotes" ADD CONSTRAINT "recast_recast_upvotes_user_id_ad942038_fk_recast_user_id" FOREIGN KEY ("user_id") REFERENCES "recast_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "recast_recast_upvotes_recast_id_cd3ca601" ON "recast_recast_upvotes" ("recast_id");
CREATE INDEX "recast_recast_upvotes_user_id_ad942038" ON "recast_recast_upvotes" ("user_id");
CREATE INDEX "recast_recast_user_id_79fe6d86" ON "recast_recast" ("user_id");
ALTER TABLE "recast_castinst" ADD CONSTRAINT "recast_castinst_actor_id_7c28b717_fk_recast_actor_id" FOREIGN KEY ("actor_id") REFERENCES "recast_actor" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "recast_castinst" ADD CONSTRAINT "recast_castinst_movie_id_06c7db13_fk_recast_movie_id" FOREIGN KEY ("movie_id") REFERENCES "recast_movie" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "recast_castinst_actor_id_7c28b717" ON "recast_castinst" ("actor_id");
CREATE INDEX "recast_castinst_movie_id_06c7db13" ON "recast_castinst" ("movie_id");
COMMIT;
