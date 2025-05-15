# ใช้ node:18-alpine เป็น base image
FROM node:18-alpine

# ตั้ง working directory
WORKDIR /app

# คัดลอก lockfile และ package.json
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./

# ติดตั้ง dependencies ตาม lockfile
RUN \
  if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
  elif [ -f package-lock.json ]; then npm ci; \
  elif [ -f pnpm-lock.yaml ]; then yarn global add pnpm && pnpm i --frozen-lockfile; \
  else echo "Lockfile not found." && exit 1; \
  fi

# คัดลอกโค้ดทั้งหมด
COPY . .

# Build frontend (ปรับตาม framework เช่น React, Vue, Next.js)
RUN npm run build
# หรือใช้ yarn/pnpm ตาม lockfile
# RUN yarn build
# RUN pnpm build

# ติดตั้ง serve เพื่อ serve static files (ถ้าเป็น static site เช่น React/Vue)
RUN npm install -g serve
# หรือใช้ dependency อื่นถ้าเป็น Next.js หรือ framework อื่น

# เปิดพอร์ต 10000 (Render ใช้พอร์ตนี้)
EXPOSE 10000

# รัน frontend
CMD ["serve", "-s", "dist", "-l", "10000"]
# ถ้าใช้ Next.js อาจใช้:
# CMD ["npm", "run", "start", "--", "-p", "10000"]
# หรือถ้าเป็น dev server:
# CMD ["npm", "run", "dev", "--", "--port", "10000"]