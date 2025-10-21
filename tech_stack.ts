// src/schemas/stack.ts
export type PriorityLevel = 'must_have' | 'should_have' | 'nice_to_have';
export type AdoptionStatus = 'current' | 'proposed' | 'deprecated';

export interface TechMetric {
  metric: string;                   // e.g. "latency_p95_ms"
  value: number | string;           // reported or expected value
  unit?: string;                    // e.g. "ms", "USD/month"
  notes?: string;                   // context or data source
}

export interface TechChoice {
  name: string;                     // e.g. "Next.js"
  version?: string;                 // e.g. "14"
  why: string;                      // rationale
  status?: AdoptionStatus;          // current vs proposed adoption state
  priority?: PriorityLevel;         // relative importance
  desired_score?: number;           // target score (0-100)
  tco_estimate_usd?: number;        // estimated total cost of ownership
  maturity?: 'experimental' | 'beta' | 'ga' | 'legacy';
  metrics?: TechMetric[];           // related quantitative metrics
  benchmarks?: string[];            // external references or benchmarks
  alternatives?: string[];          // evaluated alternatives
}

export interface ConstraintItem {
  description: string;              // e.g. "Offline support for sales"
  priority: PriorityLevel;          // must/should/nice to have
  weight?: number;                  // relative weight (0-1)
  desired_score?: number;           // desired solution score
  rationale?: string;               // constraint rationale
}

export interface OperationalContext {
  team_size?: number;               // current team size
  team_experience_level?: 'junior' | 'mixed' | 'senior';
  core_languages?: string[];        // primary languages used by the team
  annual_budget_usd?: number;       // available annual budget
  outsourcing_ratio?: number;       // percentage of outsourced work
  regulated_slas?: string[];        // mandated SLAs or regulations
  legal_requirements?: string[];    // e.g. "HIPAA", "PCI"
  customer_segments?: string[];     // primary customer segments
}

export interface TimelineConstraint {
  phase: string;                    // e.g. "MVP", "Scaling"
  start_date?: string;              // ISO-8601
  end_date?: string;                // ISO-8601
  goal?: string;                    // milestone goal
  notes?: string;                   // risks or dependencies
}

export interface HistoricalDecision {
  decision: string;                 // e.g. "Adopt PostgreSQL"
  date?: string;                    // ISO-8601
  outcome?: string;                 // observed outcome
  notes?: string;                   // key learnings
}

export interface EvaluationCriterion {
  name: string;                     // e.g. "Annual TCO"
  weight: number;                   // relative weight (0-1)
  target?: string;                  // target threshold
  description?: string;             // how to measure it
}

export interface CloudTarget {
  provider: "AWS" | "GCP" | "Azure" | "Fly.io" | "Vercel" | "Railway" | "Other";
  region?: string;        // e.g. "us-east-1", "us-central1"
  reasoning: string;      // reasoning for the chosen provider/region
}

export interface CostGuardrails {
  monthly_budget_usd?: number;      // desired budget
  cost_tactics: string[];           // e.g. "autoscaling", "spot instances"
}

export interface SecurityOps {
  auth: TechChoice;       // e.g. "Auth.js + Keycloak"
  secrets: TechChoice;    // e.g. "Doppler", "Google Secret Manager"
  policies: string[];     // e.g. "least privilege", "CIS baseline"
}

export interface Observability {
  logging: TechChoice;
  metrics: TechChoice;
  tracing?: TechChoice;
  dashboards?: string[];  // e.g. "Grafana: api-latency, error-rate"
}

export interface DataLayer {
  primary_db: TechChoice;         // e.g. "PostgreSQL 16"
  orm?: TechChoice;               // e.g. "Prisma", "SQLAlchemy"
  cache?: TechChoice;             // e.g. "Redis"
  search?: TechChoice;            // e.g. "OpenSearch", "Meilisearch"
  analytics_dw?: TechChoice;      // e.g. "BigQuery", "DuckDB"
  messaging?: TechChoice;         // e.g. "RabbitMQ", "Kafka", "Pub/Sub"
}

export interface AIModule {
  inference: TechChoice[];        // e.g. "OpenAI", "Vertex AI", "Ollama"
  vector_db?: TechChoice;         // e.g. "pgvector", "Qdrant"
  rag_pipeline?: string[];        // brief pipeline steps
  safety?: string[];              // safety policies or filters
}

export interface DevEx {
  monorepo?: boolean;
  package_manager: "pnpm" | "npm" | "yarn" | "bun";
  codegen?: string[];             // e.g. "OpenAPI → clients", "Prisma"
  ci_cd: TechChoice;              // e.g. "GitHub Actions"
  testing: {
    unit: TechChoice;
    e2e?: TechChoice;
    contract?: TechChoice;        // e.g. Pact
  };
}

export interface NFRs {
  availability_slo?: string;      // e.g. "99.9%"
  latency_p50_ms?: number;
  latency_p95_ms?: number;
  data_retention_days?: number;
  compliance?: string[];          // e.g. "GDPR", "SOC2"
  i18n_locales?: string[];        // e.g. ["es-PA", "en-US"]
}

export interface ERPxStack {
  project_name: "ERPx";
  domain_focus: string[];         // e.g. ["sales", "inventory", "accounting"]
  frontend: TechChoice[];         // e.g. Next.js, Tailwind, shadcn/ui
  backend: TechChoice[];          // e.g. FastAPI, Node/NestJS
  data: DataLayer;
  ai: AIModule;
  devops: {
    runtime: TechChoice[];        // e.g. "Docker", "Kubernetes", "Cloud Run"
    infra_as_code?: TechChoice;   // e.g. "Terraform", "Pulumi"
    deploy_target: CloudTarget;
    cost: CostGuardrails;
    observability: Observability;
    security: SecurityOps;
  };
  dev_experience: DevEx;
  nfrs: NFRs;
  constraints: ConstraintItem[];  // constraints with explicit priority
  evaluation_criteria?: EvaluationCriterion[]; // criteria to rank competing options
  operational_context: OperationalContext;     // snapshot of team and business reality
  timeline: TimelineConstraint[]; // milestones and critical deadlines
  history?: HistoricalDecision[]; // prior decisions and their outcomes
  risks: RiskItem[];
  roadmap_quickwins: string[];    // deliverables achievable in 2–4 weeks
}

export interface RiskItem {
  item: string;
  mitigation: string;
  severity?: 'low' | 'medium' | 'high';
  impacted_domains?: string[];    // e.g. ["finance", "logistics"]
}
