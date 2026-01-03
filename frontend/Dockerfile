# 1. De basis: Installeer dependencies alleen wanneer nodig
FROM node:18-alpine AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app

# Kopieer package files en installeer alles
COPY package.json package-lock.json ./
RUN npm ci

# 2. De bouwer: Bouw de broncode
FROM node:18-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Dit zorgt ervoor dat Next.js een 'standalone' map maakt
ENV NEXT_TELEMETRY_DISABLED 1
RUN npm run build

# 3. De runner: De uiteindelijke container die gaat draaien
FROM node:18-alpine AS runner
WORKDIR /app

ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

# Maak een veilige gebruiker aan (niet als admin draaien)
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

# Kopieer alleen de noodzakelijke bestanden uit de builder stage
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

# Azure Container Apps luistert standaard op poort 80, 
# maar wij hebben de app op 3000 ingesteld in je terminal-commando.
EXPOSE 3000
ENV PORT 3000
ENV HOSTNAME "0.0.0.0"

CMD ["node", "server.js"]