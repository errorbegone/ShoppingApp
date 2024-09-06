CREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(255) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL
);

CREATE INDEX "auth_permission_content_type_id_codename" ON "auth_permission" ("content_type_id", "codename");
